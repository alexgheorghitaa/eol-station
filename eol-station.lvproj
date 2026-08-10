<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="26008000">
	<Property Name="NI.LV.All.SaveVersion" Type="Str">26.0</Property>
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Bench.vi" Type="VI" URL="../station/Bench.vi"/>
		<Item Name="Bench_Tests.vi" Type="VI" URL="../station/Bench_Tests.vi"/>
		<Item Name="CheckLimit.vi" Type="VI" URL="../lib/CheckLimit.vi"/>
		<Item Name="DUT_Query.vi" Type="VI" URL="../lib/DUT_Query.vi"/>
		<Item Name="Limit_Lookup.vi" Type="VI" URL="../lib/Limit_Lookup.vi"/>
		<Item Name="Limits.ctl" Type="VI" URL="../lib/Limits.ctl"/>
		<Item Name="Load_Limits.vi" Type="VI" URL="../lib/Load_Limits.vi"/>
		<Item Name="Result.ctl" Type="VI" URL="../lib/Result.ctl"/>
		<Item Name="Scratch.vi" Type="VI" URL="../station/Scratch.vi"/>
		<Item Name="StepStatus.ctl" Type="VI" URL="../lib/StepStatus.ctl"/>
		<Item Name="Test_CellOCV.vi" Type="VI" URL="../lib/Test_CellOCV.vi"/>
		<Item Name="Test_Contactor.vi" Type="VI" URL="../lib/Test_Contactor.vi"/>
		<Item Name="Test_Iso.vi" Type="VI" URL="../lib/Test_Iso.vi"/>
		<Item Name="TestData.ctl" Type="VI" URL="../lib/TestData.ctl"/>
		<Item Name="TestState.ctl" Type="VI" URL="../lib/TestState.ctl"/>
		<Item Name="Tick.vi" Type="VI" URL="../lib/Tick.vi"/>
		<Item Name="Untitled Timestamp_ms.vi" Type="VI" URL="../lib/Untitled Timestamp_ms.vi"/>
		<Item Name="Verdict.ctl" Type="VI" URL="../lib/Verdict.ctl"/>
		<Item Name="Dependencies" Type="Dependencies"/>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
