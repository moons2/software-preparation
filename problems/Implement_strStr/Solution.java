class Solution 
{
	public static void main(String[] args)
	{
		String haystack = "hello";
		String needle = "ll";

		if(haystack.length() < needle.length())
			System.out.println(-1);

		int needleSize = needle.length();
		//		0 1 2 3 4
		// 		h e l l o
		// 	   |   |
		//
		for (int i = 0; i <= haystack.length()-needleSize; i++){
			if (haystack.substring(i, i+needleSize).equals(needle))
				System.out.println(i);
		}
		System.out.println(-1);
	}
}