
function follow_unfollow(){
    const action = $(this).attr("data-action");
    console.log('Hello!');
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
                $(this).text(data.wording);
                $(this).removeClass("btn-info").addClass("btn-danger");
                $("#follow-tag").removeClass("fa-plus").addClass("fa-minus");
            }
            else{
                //change action to follow
                $(this).attr("data-action", data.action);
                $(this).text(data.wording);
                $(this).removeClass("btn-danger").addClass("btn-outline-primary");
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
    $(document).on("click", '.follow_button',follow_unfollow);

}, 10);

