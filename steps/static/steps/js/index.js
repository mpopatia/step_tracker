function store_steps() {
    console.log("CALLED");
    steps = $('#step_count').val();
    $.get('store_steps', {'step_count': steps}, function(data){
        console.log("RESPONSE");
        console.log(data);
    });
}