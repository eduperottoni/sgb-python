def return_book_validation(book, user):
  for i in user.get_rented():
    if i == book:
      user.get_rented().remove(i)
  book.set_leased_amount(book.get_leased_amount()-1)
  return ({'valid':True, 'message':f'Livro {book.get_title()} devolvido :)'})