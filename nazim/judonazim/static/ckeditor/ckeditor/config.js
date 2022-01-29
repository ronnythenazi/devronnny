/**
 * @license Copyright (c) 2003-2021, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	// Define changes to default configuration here. For example:
         config.contentsLangDirection = 'rtl';
         config.defaultLanguage = "he";
         config.language = 'he';
        // 29/01/2022 18:14
        config.removePlugins = 'scayt,menubutton,contextmenu';
        // end 29/01/2022 18:14
};
