<alloy builddate="2012-09-25 15:54 EDT">

<instance bitwidth="4" maxseq="4" command="Check repair_assert_1" filename="">

<sig label="seq/Int" ID="0" parentID="1" builtin="yes">
</sig>

<sig label="Int" ID="1" parentID="2" builtin="yes">
</sig>

<sig label="String" ID="3" parentID="2" builtin="yes">
</sig>

<sig label="this/BinaryTree" ID="4" parentID="2" one="yes">
   <atom label="BinaryTree$0"/>
</sig>

<field label="root" ID="5" parentID="4">
   <tuple> <atom label="BinaryTree$0"/> <atom label="Node$0"/> </tuple>
   <types> <type ID="4"/> <type ID="6"/> </types>
</field>

<sig label="this/Node" ID="6" parentID="2">
   <atom label="Node$0"/>
   <atom label="Node$1"/>
</sig>

<field label="left" ID="7" parentID="6">
   <types> <type ID="6"/> <type ID="6"/> </types>
</field>

<field label="right" ID="8" parentID="6">
   <tuple> <atom label="Node$0"/> <atom label="Node$1"/> </tuple>
   <types> <type ID="6"/> <type ID="6"/> </types>
</field>

<field label="elem" ID="9" parentID="6">
   <tuple> <atom label="Node$0"/> <atom label="4"/> </tuple>
   <tuple> <atom label="Node$1"/> <atom label="5"/> </tuple>
   <types> <type ID="6"/> <type ID="1"/> </types>
</field>

<sig label="univ" ID="2" builtin="yes">
</sig>

<skolem label="$repair_assert_1_n" ID="10">
   <tuple> <atom label="Node$1"/> </tuple>
   <types> <type ID="6"/> </types>
</skolem>

</instance>

</alloy>
