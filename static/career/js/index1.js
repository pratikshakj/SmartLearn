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
        Science is the most popular and favourite career option for the majority of the parents and students.
        <br>   

        • Science stream offers many lucrative career options such as engineering, medical, IT and you can even opt for research roles.
        <br>
        • The best advantage of taking science stream is, it keeps your options open. You might switch from science to commerce or science to arts. But it is not possible to do the other way around.
        <br>
        • Taking science stream equips you with excellent problem-solving abilities. 
        <br>
        • Science and math offer a flexible foundation which enables students to accomplish highly respected and well-paid jobs.
        <br>
        • Science is fun, amazing and fascinating. As Edward Teller rightly said
        <br>
        “The science of today is the technology of tomorrow.”
        <br>
        If technology fascinates you and you have a flair for numbers, then taking science after 10th would be a wise option. 
        <br>
        - You can opt for Physics, Chemistry, Maths (PCM).
        <br>
        - If you want to make a mark for yourself in the medical field, you can opt for Physics, Chemistry, Maths, Biology (PCM-B).
        <br>
        - Now there are many students who don’t like Maths. Either they are afraid of Maths or Maths doesn’t interest them. Don’t worry, if you want to become a doctor, then knowing Maths is not necessary. You can easily opt for Physics, Chemistry, Biology (PCB).
        <br>
         There are multiple career options available for science stream after 10th class. If you have any doubts regarding what after 10th you can visit www.edumilestones.com and get your career counselling done. Their career assessment test gives 92% accurate results. 
        <br>
         It will really help you in choosing the right career stream. 
        </div>`);
        document.write("<div style='color:#ffffff;font-size:30pt;text-align:center;'><br>Good Luck!</div>");
        document.write("<div style='color:#ffffff;font-size:15pt;text-align:center;'><a href='/career/class10'>Go back</a></div>");
        document.write("</body>");
    }
    // callback to generate
    generate(i);

} 
