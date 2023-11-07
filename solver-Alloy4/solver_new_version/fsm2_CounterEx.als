<alloy builddate="2012-09-25 15:54 EDT">

<instance bitwidth="0" maxseq="0" command="Check repair_assert_1" filename="">

<sig label="seq/Int" ID="0" parentID="1" builtin="yes">
</sig>

<sig label="Int" ID="1" parentID="2" builtin="yes">
</sig>

<sig label="String" ID="3" parentID="2" builtin="yes">
</sig>

<sig label="this/FSM" ID="4" parentID="2" one="yes">
   <atom label="FSM$0"/>
</sig>

<field label="start" ID="5" parentID="4">
   <tuple> <atom label="FSM$0"/> <atom label="State$1"/> </tuple>
   <types> <type ID="4"/> <type ID="6"/> </types>
</field>

<field label="stop" ID="7" parentID="4">
   <tuple> <atom label="FSM$0"/> <atom label="State$0"/> </tuple>
   <types> <type ID="4"/> <type ID="6"/> </types>
</field>

<sig label="this/State" ID="6" parentID="2">
   <atom label="State$0"/>
   <atom label="State$1"/>
</sig>

<field label="transition" ID="8" parentID="6">
   <tuple> <atom label="State$1"/> <atom label="State$0"/> </tuple>
   <tuple> <atom label="State$1"/> <atom label="State$1"/> </tuple>
   <types> <type ID="6"/> <type ID="6"/> </types>
</field>

<sig label="univ" ID="2" builtin="yes">
</sig>

<skolem label="$repair_assert_1_s" ID="9">
   <tuple> <atom label="State$1"/> </tuple>
   <types> <type ID="6"/> </types>
</skolem>

</instance>

</alloy>
