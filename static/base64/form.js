$((e) => {
    $('#form-result').text('Anim proident aliquip excepteur amet ex. Irure ex velit reprehenderit nisi id est. Est Lorem adipisicing tempor anim esse sint tempor aliqua Lorem non ullamco ipsum irure. Ipsum dolor dolore deserunt ipsum nisi irure non excepteur. Mollit et esse do sunt.');
    $('#encode, #decode').click((e) => {
        $.post('/base64', {
            operation: $(e.currentTarget).attr('id'),
            text: $('#text-area-field').val(),
        }, (data) => {
            $('#form-result').text(data);
        }).fail((data) => {
            $('#form-result').text('Invalid input');
        });
    });
});