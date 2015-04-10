import java.text.SimpleDateFormat;

@RestController
class TimeBot {

    @RequestMapping("/")
    String home() {
		return getHead() + getBody() + getFooter();
    }

	String getHead(){
		return	"<head>" +
		"<meta charset='utf-8'>" +
		"<title>Time Bot</title>" +
		"<style>" +
			"html { overflow: hidden; margin:0; padding:0; }" +
			"body { position: absolute; top: 40%; width:100%; }" +
			"#date { font-weight:bold; } " +
			"p { text-align: center; }" +
		"</style>" +
		"</head>" +
		"<body>";
	}

	String getBody(){
		def content = "<p>Hello!<p>";
		content += "<p>";
        content += "Current time is: ";
        def date = new SimpleDateFormat( "dd MMM yyyy HH:mm:ss" );
        content += "<span id='date'>" + date.format( new Date() ) + "</span>";
		content += "</p>";
        return content;
	}

	String getFooter(){
		return "</body></html>";
	}

}
