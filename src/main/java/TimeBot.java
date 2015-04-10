import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.stereotype.*;
import org.springframework.web.bind.annotation.*;
import java.text.SimpleDateFormat;
import java.util.Date;

@RestController
@EnableAutoConfiguration
public class TimeBot {

	public static void main(String[] args) throws Exception {
        SpringApplication.run(TimeBot.class, args);
    }

    @RequestMapping("/")
    String home() {
		return TimeBot.getHead() + TimeBot.getBody() + TimeBot.getFooter();
    }

	private static String getHead(){
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

	private static String getBody(){
		String content = "<p>Hello!<p>";
		content += "<p>";
		content += "Current time is: ";
		SimpleDateFormat date = new SimpleDateFormat( "dd MMM yyyy HH:mm:ss" );
		content += "<span id='date'>" + date.format( new Date() ) + "</span>";
		content += "</p>";
        return content;
	}

	private static String getFooter(){
		return "</body></html>";
	}

}
