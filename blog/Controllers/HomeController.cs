﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace blog.Controllers
{

    [Route("/")]
    public class HomeController : Controller
    {
        // Home page
        [HttpGet]
        public string Get()
        {
            return "<h1>Blog REST API by ASP.net MVC Core</h1>";
        }
    }
}
