import java.io.*;
import java.util.*;

// 끝이 있는 Next-Permutation ([3, 2, 1] 다음 순열부터는 구하지 않음)
public class Solution {
    public static void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void reverse(int[] nums, int start) {
        int i = start;
        int j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i += 1;
            j -= 1;
        }
    }

    public static boolean nextPermutation(int[] nums){
        int i = nums.length - 1;

        // 인덱스를 뒤에서부터 탐색하며 교환 대상이 될(더 큰 값) 인덱스 위치 찾기
        while (i > 0 && nums[i - 1] >= nums[i]) {
            i -= 1;
        }

        // 인덱스가 0이되면 교환대상이 없다는 것이므로 마지막 순열임 -> 다음 순열 없음.
        if (i == 0) {
            return false;
        }

        // 바꿀 인덱스를 뒤에서 부터 탐색
        int j = nums.length - 1;
        while (nums[i - 1] >= nums[j]) {
            j -= 1;
        }

        // 찾았으면 스왑
        swap(nums, i - 1, j);

        // 역으로 스왑하면서 재정렬
        reverse(nums, i);
        return true;
    }

    public static void main(String[] args) throws Exception {
        int[] nums = { 1, 2, 3 };

        System.out.println(Arrays.toString(nums));
        while (nextPermutation(nums)) {
            System.out.println(Arrays.toString(nums));
        }
    }
}

// 끝이 없는 순열 ([3, 2, 1] 다음 순열은 [1, 2, 3])
class Solution {
    public void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public void reverse(int[] nums, int start){
        int i = start;
        int j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i += 1;
            j -= 1;
        }
    }

    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        
        // 뒤에있는 수가 앞에있는 수보다 같거나 작을때까지 인덱스 찾기
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i -= 1;
        }

        // 뒤에서부터 다시 탐색
        if (i >= 0) {
            int j = nums.length - 1;
            
            // 뒤에있는 수가 앞에있는 수보다 같거나 작을때까지 인덱스 찾기
            while (nums[j] <= nums[i]) {
                j -= 1;
            }

            // 찾았으니 스왑
            swap(nums, i, j);
        }

        // 바꾼 수열의 뒷부분을 역정렬
        reverse(nums, i + 1);
    }
}