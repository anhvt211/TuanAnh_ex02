odoo.define('employee_plus.bold',function(require){
    "use strict";
    // import packages
    var basic_fields= require('web.basic_fields');
    var registry= require('web.field_registry');

    // widget implementation
    var BoldWidget = basic_fields.FieldChar.extend({
        _renderReadonly: function() {
            this._super();b
            var old_html_render= this.$el.html();
            var new_html_render= '<b style ="color:red;">' + old_html_render + '</b>'
            console.log(11111)
            this.$el.html(new_html_render);
        }
    })

    registry.add('o_fields_bold_red', BoldWidget); // add our "bold" widget to the widget registry
})