//adapted from https://www.codexworld.com/how-to/get-selected-checkboxes-value-using-jquery/
$(document).ready(function(){
    $('#getValue').on('click', function(){
        var chkArray = [];
        
        $(".check:checked").each(function() {
            chkArray.push($(this).val());
        });
        
        // Join the array separated by the comma
        var selected;
        selected = chkArray.join("', '") ;
        
        // Check if there are selected checkboxes
        if(selected.length > 0){
            alert("Selected checkboxes value: ['" + selected + "']");	
        }else{
            alert("Please select at least one checkbox.");	
        }
    });
});