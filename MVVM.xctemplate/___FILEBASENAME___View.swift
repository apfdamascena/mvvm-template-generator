//
//  ___FILENAME___
//  ___PROJECTNAME___
//
//  Created by ___FULLUSERNAME___ on ___DATE___.
//  ___COPYRIGHT___
//

import SwiftUI

struct ___VARIABLE_ModuleName___View: View {

    @ObservedObject private var viewModel = ___VARIABLE_ModuleName___ViewModel()
       
    var body: some View {
        Text(viewModel.example ?? "Hello World")
    }

}

struct ___VARIABLE_ModuleName____Previews: PreviewProvider {
    static var previews: some View {
        ___VARIABLE_ModuleName___View()
    }
}