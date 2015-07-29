// JavaScript Document
jQuery(document).ready(function(){
		jQuery("#nav li").hover(
			function(){
				jQuery(this).children(".drop_dwon").slideDown(200);
				jQuery(this).children("#nav li a").attr("id","currlayout")
				},
			function(){
				jQuery(this).children(".drop_dwon").slideUp(100);
				jQuery(this).children("#nav li a").attr("id","")
				});
	});
	