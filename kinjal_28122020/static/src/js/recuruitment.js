odoo.define("kinjal_28122020.popupjs", function(require) {
    "use strict";

    var rpc = require("web.rpc");


    $(document).ready(function() {
        $("#state").hide();
        $("#country_id").change(function(event) {
            var country_id = $("#country_id").val();
            if(country_id==''){
                $("#state").hide();
            }
            else{
                $("#state").show();
            }
            rpc.query({
                model: "hr.applicant",
                method: "get_state",
                args: [
                    country_id,
                ],
            }).then(function(data) {
                var state_id = $('#state_id');
                state_id.empty()
                state_id.append(
                        $('<option></option>').val('').html('-----Select State-------')
                    );
                $.each(data, function(val, text) {
                    state_id.append(
                        $('<option></option>').val(val).html(text)
                    );
                });
            });
        });
    });
});
