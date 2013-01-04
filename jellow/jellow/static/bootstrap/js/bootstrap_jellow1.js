$(document).ready(function() {
        $('.list_of_paragraphs').BlocksIt({
                numOfCol: 4,
		    blockElement: '.search_article'
                    });

	$('#article').pageslide();
	
	
        $('.carousel').carousel('pause');

        var paragraph_slicing = 0;
        var heat_map = 1;
        var article_rubric = 2;
        var news_filter = 3;

        $("#paragraph_slicing").click(function(){
                $('.carousel').carousel(paragraph_slicing);
                $('.carousel').carousel('pause');
                return false;
            });

        $("#heat_map").click(function(){
                $('.carousel').carousel(heat_map);
                $('.carousel').carousel('pause');
                return false;
            });

        $("#article_rubric").click(function(){
                $('.carousel').carousel(article_rubric);
                $('.carousel').carousel('pause');
                return false;
            });

        $("#news_filter").click(function(){
                $('.carousel').carousel(news_filter);
                $('.carousel').carousel('pause');
		$('#news_filter').addClass('color_yellow');
                return false;
            });



   
    });