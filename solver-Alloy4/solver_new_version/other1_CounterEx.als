<alloy builddate="2012-09-25 15:54 EDT">

<instance bitwidth="0" maxseq="0" command="Check repair_assert_1" filename="">

<sig label="seq/Int" ID="0" parentID="1" builtin="yes">
</sig>

<sig label="Int" ID="1" parentID="2" builtin="yes">
</sig>

<sig label="String" ID="3" parentID="2" builtin="yes">
</sig>

<sig label="this/Person" ID="4" parentID="2">
   <atom label="Person$0"/>
</sig>

<field label="member_of" ID="5" parentID="4">
   <tuple> <atom label="Person$0"/> <atom label="Group$0"/> </tuple>
   <types> <type ID="4"/> <type ID="6"/> </types>
</field>

<sig label="this/alas" ID="7" parentID="6" one="yes">
   <atom label="alas$0"/>
</sig>

<sig label="this/peds" ID="8" parentID="6" one="yes">
   <atom label="peds$0"/>
</sig>

<sig label="this/Group" ID="6" parentID="2">
   <atom label="Group$0"/>
</sig>

<sig label="this/seclab" ID="9" parentID="10" one="yes">
   <atom label="seclab$0"/>
</sig>

<sig label="this/Room" ID="10" parentID="2">
   <atom label="Room$0"/>
</sig>

<field label="located_in" ID="11" parentID="10">
   <tuple> <atom label="seclab$0"/> <atom label="alas$0"/> </tuple>
   <tuple> <atom label="seclab$0"/> <atom label="peds$0"/> </tuple>
   <tuple> <atom label="seclab$0"/> <atom label="Group$0"/> </tuple>
   <types> <type ID="10"/> <type ID="6"/> </types>
</field>

<sig label="univ" ID="2" builtin="yes">
</sig>

<skolem label="$repair_assert_1_p" ID="12">
   <tuple> <atom label="Person$0"/> </tuple>
   <types> <type ID="4"/> </types>
</skolem>

</instance>

</alloy>
