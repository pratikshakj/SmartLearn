// json array movement variable
var i = 0;
var correctCount = 0 ;
//initialize the first question
generate(0);

// generate from json array data with index
function generate(index) {
    document.getElementById("question").innerHTML = jsonData[index].q;
    document.getElementById("optt1").innerHTML = jsonData[index].opt1;
    document.getElementById("optt2").innerHTML = jsonData[index].opt2;
    document.getElementById("optt3").innerHTML = jsonData[index].opt3;
}

function listDAta(data) {
    var ul=$("<ul>");
    $.each(data, function(index, value){
          ul.append($("<li>").text(value));
    });
    $('#descirption').append(ul);
}

function checkAnswer() {
    if (document.getElementById("opt1").checked && jsonData[i].opt1 == jsonData[i].answer) {
       correctCount++;
    }
    if (document.getElementById("opt2").checked && jsonData[i].opt2 == jsonData[i].answer) {
        correctCount++;
    }
    if (document.getElementById("opt3").checked && jsonData[i].opt3 == jsonData[i].answer) {
        correctCount++;
    }
    // increment i for next question
    i++;
    if(jsonData.length-1 < i){
        document.write("<body style='background-color:42917d;'>");
        document.write("<div style='color:#ffffff;font-size:25pt;text-align:center;'>Your score is : "+correctCount+"</div>");
        document.write("<div style='color:#ffffff;font-size:25pt;text-align:center;'><br>-----------------------------</div><br><br><br>");
        document.write(`
        <div id='descirption' style='color:#ffffff;font-size:18pt;text-align:center;'>
        • Nowadays arts/humanities are very high in demand and more and more students are opting for it. 
        <br>
        • Arts is now emerging as a sought after career choice. It provides students with an array of career opportunities.
        <br>
        • It offers many lucrative career options such as Journalism, languages, history, psychology etc.
        <br>
        • Design, Language Arts, Performing arts, Humanities are well-paid career options.
        <br>
        • Arts subject encourage creativity and self-expression.
        <br>
        • Students who take up art stream develop critical thinking. It also helps you increase your leadership qualities.
        <br>
        Art teaches you to deal with the world around you. 
        ~ Alan Parker.
        <br>
        If you are a student who is creative and wants to dive deep into humanity, then arts is the stream for you. 
        <br>
        There are multiple options available for Arts stream after 10th class. If you have any confusion you can get your career counselling done. A career counsellor will provide you with proper career guidance and guide you in the right direction. 
        <br>
        These are the few good career options which you can choose after 10th class.
        <br>
        </div>`);
        document.write("<div style='color:#ffffff;font-size:30pt;text-align:center;'><br>Good Luck!</div><");
        document.write("<div style='color:#ffffff;font-size:15pt;text-align:center;'><a href='/career/class10'>Go back</a></div>");
        document.write("</body>");
    }
    // callback to generate
    generate(i);

} 

