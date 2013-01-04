$(document).ready(function() {
        $('.list_of_paragraphs').BlocksIt({
                numOfCol: 4,
                    blockElement: '.search_article'
                    });
       
	$('.article').on('click',function(){
		$('#myModal').modal();
	    });

	$('.carousel').carousel({
		interval: false
		    });
	
	var paragraph_slicing = 0;
	var heat_map = 1;
	var article_rubric = 2;
	var news_filter = 3;

	$("#paragraph_slicing").hover(function(){
		$('.carousel').carousel(paragraph_slicing);
		$('.carousel').carousel({
                        interval: false
                            });
		return false;
	    });
	
	$("#heat_map").hover(function(){
                $('.carousel').carousel(heat_map);
		$('.carousel').carousel({
                        interval: false
                            });
                return false;
            });

	$("#article_rubric").hover(function(){
                $('.carousel').carousel(article_rubric);
		$('.carousel').carousel({
                        interval: false,
                            });
                return false;
            });

	$("#news_filter").hover(function(){
                $('.carousel').carousel(news_filter);
                $('.carousel').carousel({
			interval: false
			    });
                return false;
            });
    });


