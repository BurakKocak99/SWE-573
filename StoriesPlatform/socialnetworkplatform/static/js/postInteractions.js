// Initialize the map.
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 8,
    center: { lat: 40.72, lng: -73.96 },
  });
  const geocoder = new google.maps.Geocoder();
  const infowindow = new google.maps.InfoWindow();

  geocodePlaceId(geocoder, map, infowindow);

}

// This function is called when the user clicks the UI button requesting
// a geocode of a place ID.
function geocodePlaceId(geocoder, map, infowindow) {
  const placeId = document.getElementById("place-id").value;


  geocoder
    .geocode({ placeId: placeId })
    .then(({ results }) => {
      if (results[0]) {
        map.setZoom(11);
        map.setCenter(results[0].geometry.location);

        const marker = new google.maps.Marker({
          map,
          position: results[0].geometry.location,
        });

        infowindow.setContent(results[0].formatted_address);
        infowindow.open(map, marker);
      } else {
        window.alert("No results found");
      }
    })
    .catch((e) => window.alert("Geocoder failed due to: " + e));
}


function comment_action(){
    const comment_text =  document.getElementById("comment_text").value;
    if (comment_text == ""){
        return 0;
    }

    $.ajax({
        type: 'POST',
        url: "/comment",
        headers:{
            "X-CSRFToken": csrftoken,
        },
        data: {
           comment: comment_text,
           current_username: $(this).attr("curruser"),
           story_id: $(this).attr("story_id"),
        },
        success: (data) => {
            console.log(data);
            if (data.done){
                data.done = true;
                create_comment_element($(this).attr("curruser"),comment_text, "12:10");
            }
            else{
              data.done= false;
            }

        },
        error: (error) =>{
            console.warn(error);
        }
        }
    );
}


function like_action(){
     $.ajax({
        type: 'POST',
        url: "/like",
        headers:{
            "X-CSRFToken": csrftoken,
        },
        data: {
           current_username: $("#Comment_button").attr("curruser"),
           story_id: $("#Comment_button").attr("story_id"),
        },
        success: (data) => {
            console.log(data);
            if(data['done']){
                $('#likes').text(data['like_count']+" Likes")
                $('.fa-thumbs-up').removeClass(data['old_button']).addClass(data['new_button']);
            }
        },
        error: (error) =>{
            console.warn(error);
        }
        }
    );


    return 0;
}


function create_comment_element(user,comm, time){
    const root_div = document.createElement("div");
    root_div.classList.add("commented-section", "mt-2");

    const user_element = document.createElement("div");
    user_element.classList.add("d-flex", "flex-row","align-items-center","commented-user");



    const user_ref = document.createElement("a");
    user_ref.setAttribute('href',"viewprofile/"+user);
    user_ref.classList.add("text-dark", "font-weight-600");
    const h5_element = document.createElement("h5");
    h5_element.classList.add("mr-2");
    var h5_text = document.createTextNode(user);
    h5_element.appendChild(h5_text);



    user_ref.appendChild(h5_element);

    user_element.appendChild(user_ref);

    root_div.appendChild(user_element);


    const comment_element = document.createElement("div");
    comment_element.classList.add("comment-text-sm");

    const com_text = document.createElement("span");
    var span_text = document.createTextNode(comm);
    com_text.appendChild(span_text);

    comment_element.appendChild(com_text);

    root_div.appendChild(comment_element);

    const style_div1 = document.createElement("div");
    style_div1.classList.add("reply-section");

    const style_div2 = document.createElement("div");
    style_div2.classList.add("d-flex","flex-row","align-items-center","voting-icons");

    style_div1.appendChild(style_div2);

    root_div.appendChild(style_div1);


    const div_element = document.getElementById("comment_section");
    div_element.appendChild(root_div);


    document.getElementById("comment_text").value = "";


}


window.initMap = initMap;

const csrftoken= document.getElementsByName("csrfmiddlewaretoken")[0].value;


const comment_button = document.getElementById("Comment_button");
comment_button.addEventListener("click",comment_action,false);

const like_btn = document.getElementById("Like_btn");
like_btn.addEventListener("click",like_action,false);