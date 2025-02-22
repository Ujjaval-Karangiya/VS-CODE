     int s=0;
        int e= arr.length-1;
          
        while (s<=e) {
            int mid = s+(e-s)/2;
        
            if(arr[mid] > max){
                max=arr[mid];
                s=mid+1;
            }
            else if(arr[mid] < max){
                e=mid-1;
            }
           
        } 
        System.out.println("The highest peak is: "+max); 
     }
 }
