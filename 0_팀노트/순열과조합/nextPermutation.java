import java.io.*;
import java.util.*;

public class Solution {
    public static void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
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
        int k = nums.length - 1;
        while (i < k) {
            swap(nums, i, k);
            i += 1;
            k -= 1;
        }

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