const portfolioItems = document.querySelectorAll('.portfolio-item-wrapper')

  // portfolioItems.forEach(function(portfolioItem){
  //     portfolioItem.addEventListener('mouseover', ()=> {
  //         portfolioItem.childNodes[1].classList.add('img-darken');
  //     })
  //     portfolioItem.addEventListener('mouseout', ()=> {
  //         portfolioItem.childNodes[1].classList.remove('img-darken');
  //     })
  // })

portfolioItems.forEach(portfolioItem => {
      portfolioItem.onmouseover = () => {
        portfolioItem.childNodes[1].classList.add('img-darken');
      }

      portfolioItem.onmouseout = () => {
        portfolioItem.childNodes[1].classList.remove('img-darken');
      }
  })
