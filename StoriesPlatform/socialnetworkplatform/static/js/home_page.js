$(window).scroll(function() {

    if($(document).height() - ($(window).scrollTop() + $(window).height()) < 0.5) {
           console.log("Now is the time to call your server!!");
           setTimeout(get_feed, 100);

    }
});


function get_feed(){
    console.log("feed is called!!");
    const num_elements = $('#stories li').length;
    $.ajax({
        type: 'GET',
        url: 'feed',
        headers:{
            "num-elements": num_elements,
        },

        success: (data) => {

            var json_data = JSON.parse(data.content);
            console.log(json_data)
            for(let i =0; i< json_data.length; i++){
                create_feed_element(json_data[i][0],json_data[i][1],json_data[i][2], json_data[i][3], json_data[i][4], json_data[i][5], json_data[i][6]);
            }

        },
        error: (error) =>{
            console.warn(error)
        }
        }
    );

}
function create_feed_element(story_id, username, title, story, time, comments, likes){

    const author_ref = document.createElement("a"); // Author a tag
    author_ref.setAttribute('href',"viewprofile/"+username);
    var author_ref_text = document.createTextNode(username);
    author_ref.appendChild(author_ref_text);

    const author_header_div = document.createElement("div"); // Author div
    author_header_div.classList.add("activity__list__header");

    author_header_div.appendChild(author_ref); // add a tag into header div element


    const root_div = document.createElement("div"); // div element that encapsulates all items in li element

    root_div.appendChild(author_header_div); // Add header into the root div element


    const story_ref = document.createElement("a"); // View story reference in this a tag
    story_ref.setAttribute('href',"viewpost/"+story_id);
    story_ref.classList.add("text-dark", "font-weight-600");
    story_ref.style.cssText = 'text-decoration:none';




    const story_title_h2_element = document.createElement("h2");
    story_title_h2_element.classList.add("text-center");
    var story_h2_text = document.createTextNode(title);
    story_title_h2_element.appendChild(story_h2_text);


    story_ref.appendChild(story_title_h2_element);

    const story_parag = document.createElement("p");
    story_parag.classList.add("longtext");
    var story_text = document.createTextNode(story);
    story_parag.appendChild(story_text);



    const story_div = document.createElement("div"); // Story text div element
    story_div.classList.add("activity__list__body", "entry-content");


    story_div.appendChild(story_parag);

    story_ref.appendChild(story_div);

    root_div.appendChild(story_ref);// Add story reference to root div element



    const footer_div = document.createElement("div"); // this div encapsulates all of the footer elements

    footer_div.classList.add("activity__list__footer");







    const like_ref = document.createElement("a"); // like reference in this a tag
    like_ref.setAttribute('href',"viewpost/"+story_id);
    like_ref.style.cssText = 'text-decoration:none';

    const like_info = document.createElement("i");
    like_info.classList.add("fa", "fa-thumbs-up");

    like_ref.appendChild(like_info);


    var like_number = document.createTextNode(likes);

    like_ref.appendChild(like_number);


    footer_div.appendChild(like_ref);


    const comment_ref = document.createElement("a"); // comment reference in this a tag
    comment_ref.setAttribute('href',"viewpost/"+story_id);
    comment_ref.style.cssText = 'text-decoration:none';

    const comment_info = document.createElement("i");
    comment_info.classList.add("fa", "fa-comments");

    comment_ref.appendChild(comment_info);


    var comment_number = document.createTextNode(comments);

    comment_ref.appendChild(comment_number);


    footer_div.appendChild(comment_ref);


    const time_span = document.createElement("span"); // This span is for time field in the stories

    const time_info = document.createElement("i");
    time_info.classList.add("fa", "fa-clock");

    time_span.appendChild(time_info);

    const time_text = document.createTextNode(time);

    time_span.appendChild(time_text);

    footer_div.appendChild(time_span);


    root_div.appendChild(footer_div);


    const li_element = document.createElement("li");

    li_element.appendChild(root_div);


   const ul_element = document.getElementById("stories");


    ul_element.appendChild(li_element);



}