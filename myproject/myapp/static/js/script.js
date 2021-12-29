console.log('script loaded');
var statename; // mp
var subjectdetail; // all subject
const getSubject = (state) => {
  $.ajax
    ({
      type: "GET",
      url: "http://localhost:8000/getSubject?state=" + state,
      success: function (data) {
        getAll();
        console.log(data);
        subjectdetail = data;
        data = data.filter((value, index, self) =>
          index === self.findIndex((t) => (
            t?.fields?.subject === value.fields?.subject
          ))
        )

        html = '<option>Select subject</option>'
        data.forEach(element => {
          html = html + `<option value="${element?.fields?.subject}">${element?.fields?.subject}</option>`
        });
        document.getElementById("subject").innerHTML = html;
      }
    });
}

var all;
const getAll = () => {
  $.ajax
    ({
      type: "GET",
      url: "http://localhost:8000/getAll",
      success: function (data) {
        all=data;
        console.log(data);
      }

    });

}
const getState = () => {
  state = document.getElementById('state').value;
  statename = state;
  getSubject(statename);
}

const getAvrage = () => {
  selectedSubject = document.getElementById('subject').value;
  getAvrageAll();
  selectedState = statename;
  subjectAllMarks = 0;
  count = 0;
  subjectdetail.forEach( e => {
    if(e?.fields.subject === selectedSubject){
      count += 1;
      subjectAllMarks +=  e?.fields?.Marks;
    }
  })
  avrage = subjectAllMarks/ count;
  document.getElementById('disstate').innerHTML = statename;
  document.getElementById('avg').innerHTML = avrage
}

const getAvrageAll = () => {
  selectedSubject = document.getElementById('subject').value;
  selectedState = statename;
  subjectAllMarks = 0;
  count = 0;
  all.forEach( e => {
    if(e?.fields.subject === selectedSubject){
      count += 1;
      subjectAllMarks +=  e?.fields?.Marks;
    }
  })
  avrage = subjectAllMarks/ count;
  document.getElementById('disavgall').innerHTML ="All Average";
  document.getElementById('avg1').innerHTML = avrage
}