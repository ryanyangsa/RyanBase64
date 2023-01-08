import java.util.Base64;
import java.util.Base64.Decoder;
import java.util.Base64.Encoder;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;

public class RyanBase64 {
	public static void main(String[] args) throws IOException {
		if (args.length < 3) {
			System.out.println("Usage: java RyanBase64 d[e] <input> <output>");
		}

		else {
			switch (args[0]) {
				case "d":
					decode(args[1], args[2]);
					break;
				case "e":
					encode(args[1], args[2]);
					break;
				default:
					System.out.println("There are only two options: 'd' or 'e'");
					System.exit(-1);
			}
		}
	}

	public static void decode(String input, String output) throws IOException {
		byte[] in = Files.readAllBytes(Paths.get(input));
		Decoder decoder = Base64.getMimeDecoder();
		byte[] out = decoder.decode(in);
		Path filePath = Paths.get(output);
		Files.deleteIfExists(filePath);
		Files.write(filePath, out);
	}

	public static void encode(String input, String output) throws IOException {
		byte[] in = Files.readAllBytes(Paths.get(input));
		Encoder encoder = Base64.getMimeEncoder();
		byte[] out = encoder.encode(in);
		Path filePath = Paths.get(output);
		Files.deleteIfExists(filePath);
		Files.write(filePath, out);
	}
}
