package dev.laxit.productService.Controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController()
@RequestMapping("/products")
public class ProductController {

    @GetMapping
    public String getAllProducts(){
        return "Here we will return all of the available products";
    }
    @GetMapping("/{id}")
    public String getProductById(@PathVariable("id") Long id ){
        return "Here is the ProductId - "+ id;
    }

}
