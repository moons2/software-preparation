import java.io.BufferedOutputStream;
import java.io.OutputStream;

class Solution
{
    public static void main(String[] args) {
        OutputStream out = new BufferedOutputStream(System.out);

        for(int i = 999; i > 99; i--){
            try {
                out.write((i + "\n").getBytes());
            } catch (Exception e) {
                //TODO: handle exception
            } 
        }
    }
}