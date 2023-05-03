import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Dia1 {
	public static void main (String[] args){
	
	String locationFile = "/Users/rosasainz/Documents/prog/rosa/versionado/adventOfCode/2015/java/dia_1/input.txt";
	File file = new File(locationFile);

	try{
		Scanner scanner = new Scanner(file);

		while (scanner.hasNextLine()) {
			String linea = scanner.nextLine();
			System.out.print(linea);
			
		}
		scanner.close();
	} catch(IOException e){
		System.out.print("No se puede leer el archivo");
	}

	}
}