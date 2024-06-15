window.onload = function () {
  var saveAnsButton = document.getElementById("save_ans");
  saveAnsButton.onclick = saveans;

  function saveans() {
    var form = document.getElementById("quizForm");
    var ans = form.querySelector('input[name="name"]:checked');

    if (ans) {
      alert("Answer is submitted. Click next.");
      console.log(ans.value);

      var req = new XMLHttpRequest();
      var url = "/saveans?ans=" + encodeURIComponent(ans.value);

      req.open("GET", url, true);
      req.send();
    } else {
      alert("Please select an answer!");
    }
  }
};
