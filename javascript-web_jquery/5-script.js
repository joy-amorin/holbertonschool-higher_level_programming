$(document).ready(function(){

    $('#add_item').click (function() {
        const addlist = $('<li>Item</li>');
        $('.my_list').append(addlist);
    });
});
