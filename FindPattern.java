import java.io.*;

class FindPattern {

    public static void main(String[] args) {

        try {
			File file = new File("test.txt");
			FileReader fileReader = new FileReader(file);
			BufferedReader bufferedReader = new BufferedReader(fileReader);
			StringBuffer stringBuffer = new StringBuffer();
			String line;
			while ((line = bufferedReader.readLine()) != null) {
				stringBuffer.append(line);
				//stringBuffer.append("\n");
			}
			fileReader.close();
			System.out.println(stringBuffer.toString());
            if (stringBuffer.indexOf("aaaaa\\naaaaa") != -1) {
                 System.out.println("Found!");
            }
		} catch (IOException e) {
			e.printStackTrace();
		}

    }

}
