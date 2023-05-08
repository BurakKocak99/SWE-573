const csrftoken= document.getElementsByName("csrfmiddlewaretoken")[0].value;

function follow_unfollow(){
    const action = $(this).attr("data-action")
    $.ajax({
        type: 'POST',
        url: $(this).attr("data-url"),
        headers:{
            "X-CSRFToken": csrftoken,
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

window.setTimeout(() => {

    const follow_button = document.getElementById("follow_button");
    follow_button.addEventListener("click",follow_unfollow,false);

}, 10);

