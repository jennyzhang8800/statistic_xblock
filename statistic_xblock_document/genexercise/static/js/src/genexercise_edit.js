/* Javascript for PiazzaFeedXBlock. */
function GenexerciseXBlock(runtime, element) {
    $('#save',element).click(function(eventObject){
        window.location.reload(true);
    });
    var handlerAddExercise=runtime.handlerUrl(element,'addExercise');
   $("#addExercise",element).click(function(eventObject){
     var q_number=$("#qNumber").val();
     var submit_times_limit=$("#submitTimes").val();
     alert(q_number);
     alert(submit_times_limit);
     $.ajax({
        type:"POST",
        url:handlerAddExercise,
        data:JSON.stringify({"q_number":q_number,"submit_times_limit":submit_times_limit}),
        success:AddExerciseCallBack

     });
   });
    function AddExerciseCallBack(result){
     alert(result.data);
    }
}
