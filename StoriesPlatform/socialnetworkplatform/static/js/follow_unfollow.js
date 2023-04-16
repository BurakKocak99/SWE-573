

function follow_unfollow(){
    const test_element = $(this).attr("data-url");
    const action = $(this).attr("data-action")
    $.ajax({
        type: 'POST',
        url: $(this).attr("data-url"),
        headers:{
            "X-CSRFToken": getCSRFTokenValue('csrftoken'),
        },
        data: {
            action: action,
            username: $(this).attr("username"),
        },
        success: (data) => {
            console.log(data)
            $('#followerNumber').text(data.follower)
            if (action == 'follow'){
                //change to unfollow
                $(this).attr("data-action", data.action);
                $(".js-follow-text").text(data.wording);
                $(this).removeClass("btn-info").addClass("btn-danger");
                $("#follow-tag").removeClass("fa-plus").addClass("fa-minus");
            }
            else{
                //change action to follow
                $(this).attr("data-action", data.action);
                $(".js-follow-text").text(data.wording);
                $(this).removeClass("btn-danger").addClass("btn-info");
                $("#follow-tag").removeClass("fa-minus").addClass("fa-plus");
            }
        },
        error: (error) =>{
            console.warn(error)
        }
        }
    );
}
function getCSRFTokenValue(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
window.setTimeout(() => {
    const follow_button = document.getElementById("follow_button");
    follow_button.addEventListener("click",follow_unfollow,false);

}, 10);

