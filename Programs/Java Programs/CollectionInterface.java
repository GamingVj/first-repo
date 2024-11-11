// Write a program to demonstrate the method of list interface, set of interface of map.


import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;
import java.util.Set;
import java.util.Map;

public class CollectionInterface {

    public static void main(String[] args) {
        // Demonstrating List interface
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");
        list.add("Apple"); // List allows duplicate elements

        System.out.println("List elements: " + list);

        list.remove("Banana");
        System.out.println("List after removing 'Banana': " + list);

        // Demonstrating Set interface
        Set<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        set.add("Cherry");
        set.add("Apple"); // Set does not allow duplicate elements

        System.out.println("Set elements: " + set);

        set.remove("Banana");
        System.out.println("Set after removing 'Banana': " + set);

        // Demonstrating Map interface
        Map<String, Integer> map = new HashMap<>();
        map.put("Apple", 1);
        map.put("Banana", 2);
        map.put("Cherry", 3);
        map.put("Apple", 4); // Map allows duplicate keys, but the value will be updated

        System.out.println("Map elements: " + map);

        map.remove("Banana");
        System.out.println("Map after removing 'Banana': " + map);
    }
}