
$(document).ajaxComplete(function(){
   $('.profile_row > .row').mouseover(function(){
      $(this).addClass('profile-hover');});
   $('.profile_row > .row').mouseout(function(){
      $(this).removeClass('profile-hover');});
});

$(document).ajaxComplete(function(){
    $(".profile_row > .row ").click(function () {
    $content = $(this).next();
    if (!($content.is(":visible"))) {
        $(".content").slideUp("fast");
        $content.slideToggle(500);
    } else {$content.slideToggle(500);}
    });
});

$(document).ready(function(){
   $('#post-form').on("submit", function(event){
       event.preventDefault();
       var skill_field = $('#skill_field').val();
       var title_field = $('#title_field').val();
       var location_field = $('#location_field').val();
       $('#search_arg_0').html($(title_field));
       $('#search_arg_1').html($(skill_field));
       $('#search_arg_2').html($(location_field));
       var data = {"location" : location_field, "skill": skill_field, "title":title_field, "page": 1};
       search_result(data);
   });
});

$(document).ajaxComplete(function(){
    // if user clicks on the searched item and removes from the request,
    // this will call search with updated params on the first page
    var data = {
                "title": $("#search_arg_0").text(),
                "skill":  $("#search_arg_1").text(),
                "location": $("#search_arg_2").text(),
                "page": 1
    };
    $('.search_parameters > h4 > span').click(function(){
       var search_arg_id = $(this).attr("id");
       if (search_arg_id === "search_arg_0"){data['title'] = null;}
       if (search_arg_id === "search_arg_1"){data['skill'] = null;}
       if (search_arg_id === "search_arg_2"){data['location'] = null;}
       $(this).hide('fast', function(){$(this).remove();});
       search_result(data)
   });
});

function search_result(data){
    $.ajax({
        url: '/search/result/',
        type: 'POST',
        data: {location: data['location'],
               title: data['title'],
               skill: data['skill'],
               page: data['page']},
        beforeSend: function(){
                       $(".container").html('<div class="text-center"><img src="/static/images/ajax-loader.gif"></div>');
                   },
        success : function(data) {
            $(".container").html("");
            $('.profile_row').each(function(index){
               $(this).remove();});
            highlight_searched_keywords(".search_parameters > h4", ".search_parameters", data['search_args']);
            if (data['empty_search_args'] === true) {
                $(".container").append('<div class="profile_row">Nothing To Search</div>');
                $('.pagination > li').each(function(index){
                    $(this).remove();});
            } else {
                if (data['profiles'].length === 0) {
                    $(".container").append('<div class="profile_row">No Results</div>');
                    $('.pagination > li').each(function(index){
                        $(this).remove();});
                } else {
                    for (var i = 0; i < data['page_limit']; i++) {
                        var new_row = $("<div style='display: none' class='profile_row'id='profile_" + data['profiles'][i]['pk'] + "'><div class='row'>" +
                            "<div class='col-lg-1'><div class='profile_email_icon'><a href=''><img src=''></a></div></div>" +
                            "<div class='col-lg-5'><div class='profile_name'>" + data['profiles'][i]['name'] + "</div></div>" +
                            "<div class='col-lg-5'><div class='profile_title'>" + data['profiles'][i]['title'] + "</div></div>" +
                            "<div class='col-lg-1'><div class='profile_url'><a href='" + data['profiles'][i]['url'] + "' target='_blank'><img src='' title='URL'></a></div></div>" +
                            "</div>" +
                            "<div class='content' style='display:none'><div class='custom-well'><div class='profile_contacts'><div class='well-sm' style='margin: 10px'><div class='full_description'></div><div class='if_email'><img src=''><div class='profile_email' style='display: inline-block'></div></div>" +
                            "<div class='if_phone'><img src='''><div class='profile_phone' style='display: inline-block'></div></div></div></div></div>" +
                            "<div class='custom-well'><div class='well-sm' style='margin: 10px'><div class='skills_list'></div></div></div></div>");
                        $(".container").append(new_row);

                        var this_profile = $('#profile_' + data['profiles'][i]['pk']);
                        $(this_profile).find('.full_description').append("<a href='/profile/" + data['profiles'][i]['pk'] + "/' target='_blank' class='btn btn-info'>Info</a>");

                        create_contacts(this_profile, data['profiles'][i]['email'], data['profiles'][i]['phone'], data['profiles'][i]['url']);
                        create_skills(this_profile, data['profiles'][i]['skills'], data['search_args']);
                        new_row.show('fast');
                        paginator(data, data['page']);
                    }
                }
            }
         }
    });
}
function paginator(data, current_page) {
    var paginator = $('.pagination');
    var page_numbers = data['number_of_pages'];
    $(paginator).find('li').each(function () {
        $(this).remove()
    });
    if (page_numbers > 5) {
        if (current_page == 1) {
            $(paginator).append('<li class="active"><a id="page_' + current_page + '" href="#">' + current_page + '</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page + 1) + '" href="#">' + (current_page + 1) + '</a></li>');
            $(paginator).append('<li><a id="page_..." href="#">...</a></li>');
            $(paginator).append('<li><a id="page_' + page_numbers + '" href="#">' + page_numbers + '</a></li>');
        } else if (current_page == 2) {
            $(paginator).append('<li><a id="page_' + (current_page - 1) + '" href="#">' + (current_page - 1) + '</a></li>');
            $(paginator).append('<li class="active"><a id="page_' + current_page + '" href="#">' + current_page + '</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page + 1) + '" href="#">' + (current_page + 1) + '</a></li>');
            $(paginator).append('<li><a id="page_..." href="#">...</a></li>');
            $(paginator).append('<li><a id="page_' + page_numbers + '" href="#">' + page_numbers + '</a></li>')
        } else if (current_page == 3) {
            $(paginator).append('<li><a id="page_1" href="#">1</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page - 1) + '" href="#">' + (current_page - 1) + '</a></li>');
            $(paginator).append('<li class="active"><a id="page_' + current_page + '" href="#">' + current_page + '</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page + 1) + '" href="#">' + (current_page + 1) + '</a></li>');
            $(paginator).append('<li><a id="page_..." href="#">...</a></li>');
            $(paginator).append('<li><a id="page_' + page_numbers + '" href="#">' + page_numbers + '</a></li>')
        } else if (current_page >= 2 && page_numbers - 2 > current_page) {
            $(paginator).append('<li><a id="page_1" href="#">1</a></li>');
            $(paginator).append('<li><a id="page_..." href="#">...</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page - 1) + '" href="#">' + (current_page - 1) + '</a></li>');
            $(paginator).append('<li class="active"><a id="page_' + current_page + '" href="#">' + current_page + '</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page + 1) + '" href="#">' + (current_page + 1) + '</a></li>');
            $(paginator).append('<li><a id="page_..." href="#">...</a></li>');
            $(paginator).append('<li><a id="page_' + page_numbers + '" href="#">' + page_numbers + '</a></li>')
        } else if (current_page == page_numbers - 2) {
            $(paginator).append('<li><a id="page_1" href="#">1</a></li>');
            $(paginator).append('<li><a id="page_..." href="#">...</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page - 1) + '" href="#">' + (current_page - 1) + '</a></li>');
            $(paginator).append('<li class="active"><a id="page_' + current_page + '" href="#">' + current_page + '</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page + 1) + '" href="#">' + (current_page + 1) + '</a></li>');
            $(paginator).append('<li><a id="page_' + page_numbers + '" href="#">' + page_numbers + '</a></li>')
        } else if (current_page == page_numbers - 1) {
            $(paginator).append('<li><a id="page_1" href="#">1</a></li>');
            $(paginator).append('<li><a id="page_..." href="#">...</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page - 1) + '" href="#">' + (current_page - 1) + '</a></li>');
            $(paginator).append('<li class="active"><a id="page_' + current_page + '" href="#">' + current_page + '</a></li>');
            $(paginator).append('<li><a id="page_' + page_numbers + '" href="#">' + page_numbers + '</a></li>')
        } else if (current_page == page_numbers) {
            $(paginator).append('<li><a id="page_1" href="#">1</a></li>');
            $(paginator).append('<li><a id="page_..." href="#">...</a></li>');
            $(paginator).append('<li><a id="page_' + (current_page - 1) + '" href="#">' + (current_page - 1) + '</a></li>');
            $(paginator).append('<li class="active"><a id="page_' + current_page + '" href="#">' + current_page + '</a></li>');
        }
    } else if (page_numbers < 5) {
        for (var i = 1; i < page_numbers + 1; i++) {
            if (current_page == i){
                $(paginator).append('<li class="active"><a id="page_"' + i + ' href="#">' + i + '</a></li>');
            } else {
                $(paginator).append('<li><a id="page_"' + i + ' href="#">' + i + '</a></li>');
            }
        }
    }
}
function highlight_searched_keywords(selector_row, selector_box, searched_args){
    $(selector_row).each(function(){$(this).remove();});
    for (var j =0; j < searched_args.length; j++){
        $(selector_box).append('<h4 style="margin: 5px; margin-bottom:10px; display: inline-block"><span id="search_arg_' + j + '" class="label label-default" style="color: green">'+ searched_args[j] + '</span></h4>');
    }
}
function create_contacts(profile_id, profile_email, profile_phone, url){
    $(profile_id).find('.profile_url > a').attr('href', url);
    $(profile_id).find('.profile_url > a > img').attr('src', "/static/images/linkedin_icon.png");
    if (profile_email){
        $(profile_id).find('.profile_email_icon > a >img').attr('src', "/static/images/tick.png");
        $(profile_id).find('.profile_contacts > .well-sm > .if_email > img').attr('src', "/static/images/email green.png");
        $(profile_id).find('.profile_email').html(profile_email)}
    else {
        $(profile_id).find('.profile_email_icon > a >img').attr('src', "/static/images/minus.png")
    }
    if (profile_phone){
        $(profile_id).find('.profile_contacts > .well-sm > .if_phone > img').attr('src', "/static/images/phone.png");
        $(profile_id).find('.profile_phone').html(profile_phone)
    }
}
function create_skills(profile_id, skills, searched_args){
    for (var skill = 0; skill < skills.length; skill++) {
        if (jQuery.inArray(skills[skill], searched_args) === -1) {
            $(profile_id).find('.skills_list').append("<h4 style='margin: 5px; margin-bottom:10px; display: inline-block'><span class='label label-default'>" + skills[skill] + "</span></h4>")
        } else {
            $(profile_id).find('.skills_list').append("<h4 style='margin: 5px; margin-bottom:10px; display: inline-block'><span class='label label-default' style='color:green'>" + skills[skill] + "</span></h4>")
        }
    }
}
$(document).ajaxComplete(function(){
   $('.pagination > li > a').click(function() {
       var page = $(this).text();
       var data = {
           "title": $("#search_arg_0").text(),
           "skill": $("#search_arg_1").text(),
           "location": $("#search_arg_2").text(),
           "page": page};
           search_result(data);
   });
});

