import socket, random

HOST, PORT = "127.0.0.1", 5025
NCELLS = 96
CELLS_PER_FRAME = 4
BASE_ID = 0x320

class Pack:
    def __init__(self, seed=123, golden=False):
        self.seed, self.golden = seed, golden
        r = random.Random(seed)
        self.serial = "SN-GOLDEN" if golden else f"SN-{seed:06d}"
        if golden:
            self.cells = [3.7000] * NCELLS
            self.iso, self.contactors, self.fault = 10.00, False, None
            return
        self.soc = 0.45 + (seed % 21) / 100.0
        base = 3.0 + 1.2 * self.soc
        self.cells = [round(base + r.uniform(-0.02, 0.02), 4) for _ in range(NCELLS)]
        self.iso = round(5.0 + r.uniform(0, 15), 2)
        self.contactors = False
        self.fault = None
        if seed % 5 == 0:
            self.fault = ["BADCELL", "ISO", "CONT", "BADCELL"][(seed // 5) % 4]
            if self.fault == "BADCELL":
                self.cells[42] = 3.31
            elif self.fault == "ISO":
                self.iso = 0.4

    def pack_v(self):
        return round(sum(self.cells), 2)

    def frames(self):
        out = []
        for f in range(NCELLS // CELLS_PER_FRAME):
            payload = ""
            for k in range(CELLS_PER_FRAME):
                mv = int(round(self.cells[f * CELLS_PER_FRAME + k] * 1000))
                payload += f"{mv:04X}"
            out.append(f"{BASE_ID + f:03X}:{payload}")
        return out

def handle(cmd, pack):
    cmd = cmd.strip(); head = cmd.split(" ")[0].upper(); arg = cmd[len(head):].strip()
    if head == "*IDN?":              return f"SIMU,BP96,{pack.serial},FW1.0"
    if head == "MEAS:ISO?":          return f"{pack.iso:.2f}"
    if head == "MEAS:VOLT:CELL?":
        try: n = int(arg)
        except ValueError: return "ERR,SYNTAX"
        if not 0 <= n < NCELLS: return "ERR,RANGE"
        return f"{pack.cells[n]:.4f}"
    if head == "MEAS:CELL:BURST?":   return ";".join(pack.frames())
    if head == "MEAS:VOLT:PACK?":
        return f"{pack.pack_v():.2f}" if pack.contactors else "ERR,CONT_OPEN"
    if head == "SYS:CONT":
        if arg.upper() == "CLOSE":
            if pack.fault == "CONT": return "ERR,CONT_FAULT"
            pack.contactors = True;  return "OK"
        pack.contactors = False;     return "OK"
    if head == "SYS:GOLDEN":
        pack.__init__(0, golden=True); return "OK,SN-GOLDEN"
    if head == "SYS:NEWUUT":
        try: seed = int(arg)
        except ValueError: return "ERR,SYNTAX"
        pack.__init__(seed); return f"OK,{pack.serial}"
    return "ERR,SYNTAX"

def main():
    pack = Pack(123)
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT)); srv.listen(1)
    print(f"listening on {HOST}:{PORT}")
    while True:
        conn, _ = srv.accept(); buf = b""
        with conn:
            while True:
                chunk = conn.recv(4096)
                if not chunk: break
                buf += chunk
                while b"\n" in buf:
                    line, buf = buf.split(b"\n", 1)
                    reply = handle(line.decode("utf-8", "replace"), pack)
                    conn.sendall((reply + "\r\n").encode())

if __name__ == "__main__":
    main()
