function retrieve(id) {
    const form = document.getElementById(id)
    const input = form.getElementsByTagName("input")
    let usrname = input[0].value
    let usrsubject = input[1].value
    let usremail = input[2].value
    let usrmessage = document.getElementById("usrmessage").value
    console.log(usrmessage);
    const data = {
        name: usrname,
        subject: usrsubject,
        email: usremail,
        message: usrmessage
    }

    fetch(
        "https://o8kdvuahw4.execute-api.us-west-2.amazonaws.com/emailTest",
        {method: 'POST',
        header: {
            'Content-Type': 'applications/json'
        },
        body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((data) => {
        alert('Successfully submitted, we\'ll be in touch!');
    })
    .catch((error) => {
        alert('Please try again.');
    })
}