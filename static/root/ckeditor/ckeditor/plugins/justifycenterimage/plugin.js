/**
* Justify center images plugin for CKEditor
* Licensed under the MIT license
* http://github.com/mabarroso/CKEditor-JustifyCenterImage-Plugin
* Plugin for: http://ckeditor.com/license (GPL/LGPL/MPL: http://ckeditor.com/license)
*/

CKEDITOR.plugins.add( 'justifycenterimage',
{
    init: function( editor )
    {
        editor.addCommand( 'justifycenterimage',
        {
            exec : function( editor )
            {
                var type = editor.getSelection().getType();
                var imageElement = editor.getSelection().getSelectedElement();
                if ((type != 3) || (imageElement.getName() != 'img') ) {
                    editor.execCommand('justifycenter', false, null);
                } else {
                    imageElement.setStyle('float','none');
                    var newElement = new CKEDITOR.dom.element("p");
                    newElement.setStyle('text-align','center');
                    imageElement.move(newElement);
                    editor.insertElement(newElement);
                }
            }
        });
        editor.ui.addButton( 'JustifyCenterImage',
        {
            label : editor.lang.justify.center,
            command: 'justifycenterimage',
            icon: this.path + 'images/justifycenterimage.png'
        } );
    }
} );