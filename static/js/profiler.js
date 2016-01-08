/**
 * Created by Alex on 07/01/2016.
 */



$(document).ready(function(){
    $('#add_comment').click(function(){

       data = {'profile_id': $('.hidden_profile_id').text(),
               'comment_text': $('#text_field').val(),
                "selected_opening": $('.filter-option.pull-left').text()
       };
       $('#text_field').val("");
       add_comment(data);
    });
});

function add_comment(data){
    var url = '/profile/' + data['profile_id'] + '/add_comment/';
    $.ajax({
        url: url,
        type: 'POST',
        data: { profile_id: data['profile_id'],
                comment_text: data['comment_text'],
                selected_opening: data['selected_opening']
        },
        success: function (data) {
        $('.profile_comment_box').append('<li>' + data['comments']['comment_author'] +
                                                          ' / '  + data['comments']['comment_date'] +
                                                          ' / '  + data['comments']['comment_vacancy'] +
                                                          ' / '  + data['comments']['comment_text'] +
                    '</li>');}
    })
}


$(document).ready(function(){
    setInterval(show_all_comments, 1000)
});

function show_all_comments(){
    data = {'profile_id': $('.hidden_profile_id').text()};
    var url = '/profile/' + data['profile_id'] + '/all_comments/';
    $.ajax({
        url: url,
        type: 'POST',
        data: { profile_id: data['profile_id']},
        success: function (data) {
            $('.profile_comment_box').find('li').each(function () {$(this).remove();});

            for (var i = 0; i < data['comments'].length; i++) {
                $('.profile_comment_box').append('<li>' + data['comments'][i]['comment_author'] +
                                                          ' / '  + data['comments'][i]['comment_date'] +
                                                          ' / '  + data['comments'][i]['comment_vacancy'] +
                                                          ' / '  + data['comments'][i]['comment_text'] +
                    '</li>');
            }

        }
    });
}