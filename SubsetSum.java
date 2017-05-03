import java.util.Arrays;


public class SubsetSum {

    public static void main(String[] args) {

        int[] nums = {1, 2, 5, 4, 5, 6, 7};
        System.out.println(doesContainSubSum(nums));

    }

    static boolean doesContainSubSum(int[] arr) {

        for (int i = 0; i < arr.length - 1; i++) {
            int complement = arr[i] * -1;
            if (Arrays.binarySearch(arr, i + 1, arr.length - 1, complement) > 0) {
                return true;
            }

        }

        return false;

    }

}
