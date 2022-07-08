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
        • Commerce is also one of the most popular career. If you love numbers, finances, economics etc., then finance is the best option for you.
        <br>
        • It offers a wider variety of career options such as Chartered Accountants, MBA, investment in banking sectors etc.
        <br>
        • You acquire commercial knowledge which is very important for the business.
        <br>
        • You have to be familiar with the subjects such as Accountancy, Finance, Economics etc.
        <br>
        • You must be good with numbers, data and have a curiosity in Finance, economics. 
        <br>
        If you have an affinity for numbers, business, economics then commerce is the stream for you. 
        <br>
        If you want to shape your career in economics and business world, then commerce is the right career for you. 
        <br>
T       here are a number of options available for commerce stream after 10th class. If you have any doubts regarding whether to opt for commerce stream you can choose the smartest way by getting your career counselling done from an expert. Proper career guidance after 10th class is extremely necessary for a hassle-free career. Edumilestones career assessment is considered to be the best by the industry experts. Their career assessment is tested on statistical methodologies and provides accurate and reliable results. 
        <br>
        • Commerce as a subject is gaining popularity in India and many students are studying and making a living out of it. 
        </div>`);
        document.write("<div style='color:#ffffff;font-size:30pt;text-align:center;'><br>Good Luck!</div>");
        document.write("<div style='color:#ffffff;font-size:15pt;text-align:center;'><a href='/career/class10'>Go back</a></div>");
        document.write("</body>");
    }
    // callback to generate
    generate(i);

} 
