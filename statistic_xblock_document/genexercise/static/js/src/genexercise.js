/* Javascript for PiazzaFeedXBlock. */
function GenexerciseXBlock(runtime, element) {
    function showResult(result){
      $('#tips').innerHTML=""
      $('#iframepage').hide();
      $('#iframepage').attr('src',$('#iframepage').attr('src'));
      $('#iframepage').show();
    }
    var handlerUrlStatistic = runtime.handlerUrl(element,'statistic_click');
    $('#statisticBtn',element).click(function(eventObject){
      $('#tips').innerHTML="statistic,please wait..."
      $.ajax({
            type:"POST",
            url:handlerUrlStatistic,
            data:JSON.stringify({"statistic":"yes"}),
            success:showResult
      });
    });
    $(function ($) {
        /* Here's where you'd do things on page load. */
      $('#iframepage').hide();
       
    });
}
