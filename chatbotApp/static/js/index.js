var msgArray = [];

$(document).ready(function () {
    console.log("Chatbot Running..")
    $(document).on('click', '#send_button', function (e) {
        e.preventDefault();
        var formDataSerialized = new FormData($('#myForm')[0]);

        ajax_call(formDataSerialized)
        msgArray.push(formDataSerialized)
        console.log('On Send Button Click - Message Array : '.concat(msgArray))
    })
});

function SelectOptionValue(option) {
    console.log('Option selected : '.concat(option))
    document.getElementById('title').value = '';
    document.getElementById('msgType').value = option;
    if (option == 'About Us') {
        document.getElementById('myForm').style.display = 'none';
    }
    else {
        document.getElementById('myForm').style.display = 'block';
    }

    var csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
    var formData = new FormData();
    formData.append('title', '');
    formData.append('msgType', option);
    formData.append('csrfmiddlewaretoken', csrfmiddlewaretoken)
    ajax_call(formData)

}

function EnableDisable(title) {
    //Reference the Button.
    var btnSubmit = document.getElementById("send_button");

    //Verify the TextBox value.
    if (title.value.trim() != "") {
        //Enable the TextBox when TextBox has value.
        btnSubmit.disabled = false;
        btnSubmit.style.opacity = 1;
    } else {
        //Disable the TextBox when TextBox is empty.
        btnSubmit.disabled = true;
    }
};


function ajax_call(formDataValue) {
    $.ajax({
        url: "",
        type: 'POST',
        data: formDataValue,
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            console.log(data)
            var chat = ""
            var new_date = new Date();
            if (new_date.getHours() < 12) {
                time_extension = " AM"
            }
            else {
                time_extension = " PM"
            }
            var new_time = new_date.toLocaleTimeString();
            var local_time = new_time.substr(0, 5)


            chat += '<div class="incoming_msg">';
            chat += '<div class="incoming_msg_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="bot_img"> </div>';
            chat += '<div class="received_msg">';
            chat += '<div class="overlay-text">';
            chat += '<div class="received_withd_msg">';
            chat += '<p id="p_input">' + data.msg + '</p>';
            chat += '<span class="time_date">' + local_time.concat(time_extension) + '</span></div>';
            chat += '</div>';
            chat += '</div>';
            chat += '<div class="outgoing_msg">';
            chat += '<div class="sent_msg_img"> <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--4nVcu5jx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://cdn.dribbble.com/users/722835/screenshots/4082720/bot_icon.gif" alt="user_img"> </div>';
            chat += '<div class="sent_msg">';
            chat += '<div class="overlay-text">';
            chat += '<p id="p_input2">' + data.ans + '</p>';
            chat += '<span class="time_date">' + local_time.concat(time_extension) + '</span> </div>';
            chat += '</div>';
            $('#msg').append(chat)
            // $('#p_input').html(data.msg)
            // $('#p_input2').html(data.ans)
            $('#title').val('')

            $("html, body").animate({
                scrollTop: $('html, body').get(0).scrollHeight
            }, 2000);
        }
    });
}
