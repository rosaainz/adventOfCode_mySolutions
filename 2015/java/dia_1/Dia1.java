import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Dia1 {
	public static void main (String[] args){
		try{
			File file = new File("/Users/rosasainz/Documents/prog/rosa/versionado/adventOfCode_mySolutions/2015/java/dia_1/input.txt");
			Scanner scanner = new Scanner(file);

			while(scanner.hasNextLine()){
				String line = scanner.nextLine();
				System.out.print(line);
			}

			scanner.close();
		} catch(IOException e){
			System.out.print("No se puede leer el archivo");
		}

	}
}