/**
 * Created with PyCharm.
 * User: jennyzhang
 * Date: 16-3-11
 * Time: 下午4:46
 * To change this template use File | Settings | File Templates.
 */




//初始时显示课程的所有练习题完成情况
window.onload=function(){
//页面加载时feed部分显示的是my_feed的内容


    showTemplate();


}


//下一页
function next() {

    hideTable();

    currentRow = pageSize * page;
    maxRow = currentRow + pageSize;
    if (maxRow > numberRowsInTable) maxRow = numberRowsInTable;
    for (var i = currentRow; i < maxRow; i++) {
        theTable.rows[i].style.display = '';
    }
    page++;

    if (maxRow == numberRowsInTable) { nextText(); lastText(); }
    showPage();
    preLink();
    firstLink();
}


//上一页
function pre() {
    hideTable();
    page--;
    currentRow = pageSize * page;
    maxRow = currentRow - pageSize;
    if (currentRow > numberRowsInTable) currentRow = numberRowsInTable;
    for (var i = maxRow; i < currentRow; i++) {
        theTable.rows[i].style.display = '';
    }

    if (maxRow == 0) { preText(); firstText(); }
    showPage();
    nextLink();
    lastLink();
}

//第一页
function first() {
    hideTable();
    page = 1;
    for (var i = 0; i < pageSize; i++) {
        theTable.rows[i].style.display = '';
    }
    showPage();
    preText();
    nextLink();
    lastLink();
}


//最后一页
function last() {
    hideTable();
    page = pageCount();
    currentRow = pageSize * (page - 1);
    for (var i = currentRow; i < numberRowsInTable; i++) {
        theTable.rows[i].style.display = '';
    }
    showPage();
    preLink();
    nextText();
    firstLink();
}


function hideTable() {
    for (var i = 0; i < numberRowsInTable; i++) {
        theTable.rows[i].style.display = 'none';
    }
}


function showPage() {
    pageNum.innerHTML = page;
}


//总共页数
function pageCount() {
    var count = 0;
    if (numberRowsInTable % pageSize != 0) count = 1;
    return parseInt(numberRowsInTable / pageSize) + count;
}


//显示链接
function preLink() { spanPre.innerHTML = "<a href='javascript:pre();'>上一页</a>"; }
function preText() { spanPre.innerHTML = "上一页"; }


function nextLink() { spanNext.innerHTML = "<a href='javascript:next();'>下一页</a>"; }
function nextText() { spanNext.innerHTML = "下一页"; }


function firstLink() { spanFirst.innerHTML = "<a href='javascript:first();'>第一页</a>"; }
function firstText() { spanFirst.innerHTML = "第一页"; }


function lastLink() { spanLast.innerHTML = "<a href='javascript:last();'>最后一页</a>"; }
function lastText() { spanLast.innerHTML = "最后一页"; }


//隐藏表格
function hide() {
    for (var i = pageSize; i < numberRowsInTable; i++) {
        theTable.rows[i].style.display = 'none';
    }
    totalPage.innerHTML = pageCount();
    pageNum.innerHTML = '1';
    nextLink();
    lastLink();
}

//显示课程的所有练习题完成情况
function showTemplate(){

    //注册索引+1的helper
    var handleHelper = Handlebars.registerHelper("addOne",function(index){
      //返回+1之后的结果
    return index+1;
    });
    url_github="https://raw.githubusercontent.com/jennyzhang8800/statistic_xblock/master/statisticByExercise.json";
    $.ajax({
        type : "get",
        cache : false,
        url : url_github , // 请求地址
        success : function(data_i) { // ajax执行成功后执行的方法


             data = eval("(" + data_i + ")") // 把string转化为json
            alert(data.total_submitted_count);
            var source   = $("#table-template").html();
            var template = Handlebars.compile(source);
            $("#tableDiv").html(template(data));


        }
    });

    altRows('alternatecolor');
    //分页显示
    theTable = document.getElementById("table3");
    totalPage = document.getElementById("spanTotalPage");
    pageNum = document.getElementById("spanPageNum");

    spanPre = document.getElementById("spanPre");
    spanNext = document.getElementById("spanNext");
    spanFirst = document.getElementById("spanFirst");
    spanLast = document.getElementById("spanLast");

    numberRowsInTable = theTable.rows.length;
    pageSize = 40;
    page = 1;
    hide();

}

//根据题号，显示提交的该题的所有用户
function ShowUsers(qNumber){

    showTemplateUser(qNumber);
    //分页显示
    theTable = document.getElementById("table4");
    totalPage = document.getElementById("spanTotalPage");
    pageNum = document.getElementById("spanPageNum");

    spanPre = document.getElementById("spanPre");
    spanNext = document.getElementById("spanNext");
    spanFirst = document.getElementById("spanFirst");
    spanLast = document.getElementById("spanLast");

    numberRowsInTable = theTable.rows.length;
    pageSize = 40;
    page = 1;

    hide();

}

//根据用户名，显示该用户所提交的题
function ShowQNumberList(userName){
var qListByName={}
var qNumberList=[]

for(var i=0; i<data.children.length;i++){
       for(var j=0; j<data.children[i].user_name_list.length;j++){
           if(data.children[i].user_name_list[j]==userName){
              qNumberList.push(data.children[i].q_number);
           }
            
        }
       
    }
qListByName["qNumberList"]=qNumberList

    //注册索引+1的helper
    var handleHelper = Handlebars.registerHelper("addOne",function(index){
        //返回+1之后的结果
        return index+1;
    });

   
    var source   = $("#user-qnumber-table-template").html();
    var template = Handlebars.compile(source);

    
   
    $("#tableDiv").html(template(qListByName));
    CurrentqNumber = document.getElementById("userName");
    CurrentqNumber.innerHTML = "(用户:"+userName+")";
    var exerciseCount= document.getElementById("exerciseCount");
    exerciseCount.innerHTML="&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp该用户提交了<span style='color:red'>"+qNumberList.length+"</span>道题"
   
    altRows('alternatecolor-user-qnumber');
    theTable = document.getElementById("table5");
    totalPage = document.getElementById("spanTotalPage");
    pageNum = document.getElementById("spanPageNum");

    spanPre = document.getElementById("spanPre");
    spanNext = document.getElementById("spanNext");
    spanFirst = document.getElementById("spanFirst");
    spanLast = document.getElementById("spanLast");

    numberRowsInTable = theTable.rows.length;
    pageSize = 40;
    page = 1;
    hide();




}

//根据题号，显示提交了该题的所有用户
function showTemplateUser(qNumber){
    //注册索引+1的helper
    var handleHelper = Handlebars.registerHelper("addOne",function(index){
        //返回+1之后的结果
        return index+1;
    });

   
    var source   = $("#user-table-template").html();
    var template = Handlebars.compile(source);
    

    var user_list={};
   
    user_list["user_name_list"]=[]
    
    for(var i=0; i<data.children.length;i++){
       if(data.children[i].q_number==qNumber){user_list["user_name_list"]=data.children[i].user_name_list;break;}
       
    }
    
   
    $("#tableDiv").html(template(user_list));
    CurrentqNumber = document.getElementById("qNumber");
    CurrentqNumber.innerHTML = "(题号:"+qNumber+")";
    var userCount= document.getElementById("userCount");
    userCount.innerHTML="&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp本题共有<span style='color:red'>"+user_list["user_name_list"].length+"</span>个用户提交"
    altRows('alternatecolor-user');

}

//表格样式，自动隔行换色
function altRows(id){
    if(document.getElementsByTagName){

        var table = document.getElementById(id);
        var rows = table.getElementsByTagName("tr");

        for(i = 0; i < rows.length; i++){
            if(i % 2 == 0){
                rows[i].className = "evenrowcolor";
            }else{
                rows[i].className = "oddrowcolor";
            }
        }
    }
}
