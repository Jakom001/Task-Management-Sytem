
$(document).ready(function(id){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();

	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;
			});
		} else{
			checkbox.each(function(){
				this.checked = false;
			});
		}
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});

$(".edit").click(function() {
  var id = $(this).attr("id").split("_")[1]
  $(`#editEmployeeModal_${id}`).show();
});

$(".ebcf_close").click(function() {
  $(".ebcf_modal").hide();
});

    
$(document).ready(function () {
    $('#task_table').DataTable();
});



