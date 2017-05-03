import java.util.Arrays;

class sortPossible {

    public static void main(String[] args) {

        int[] arr = {4, 5, 8, 7};

        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i+1] && Math.abs(arr[i] - arr[i+1]) == 1) {
                int tmp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = tmp;

            }

        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
        }

        boolean sorted = true;
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i+1]) {
                sorted = false;
            }
        }

        System.out.println(sorted);




    }


}
