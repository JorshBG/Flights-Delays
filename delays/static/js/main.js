/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
// Call the dataTables jQuery plugin
$(document).ready(function () {
    $('.datasets-datatable').DataTable({
        lengthMenu: [5, 10, 15, 20]
    });
});
